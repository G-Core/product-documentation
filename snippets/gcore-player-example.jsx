import { useEffect, useId, useRef } from "react";

export const GcorePlayerExample = ({ source }) => {
  const resolvedSource =
    source ||
    "https://demo-public.gvideo.io/videos/2675_w6nGXEimHz4Z6t1j/master.m3u8";
  const reactId = useId();
  const containerRef = useRef(null);
  const playerIdRef = useRef(`gcore-player-${reactId.replace(/[:]/g, "-")}`);

  useEffect(() => {
    if (!containerRef.current) {
      return;
    }

    const playerCssUrl = "https://player.gvideo.co/v2/assets/latest/index.css";
    const playerModuleUrl = "https://player.gvideo.co/v2/assets/latest/index.js";
    const selectionResetStyleId = "gcore-player-selection-reset";

    if (!document.querySelector(`link[href="${playerCssUrl}"]`)) {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = playerCssUrl;
      document.head.appendChild(link);
    }

    if (!document.getElementById(selectionResetStyleId)) {
      const style = document.createElement("style");
      style.id = selectionResetStyleId;
      style.textContent = `
        body, body * {
          -webkit-user-select: text !important;
          user-select: text !important;
          -webkit-touch-callout: default !important;
        }

        #${playerIdRef.current}, #${playerIdRef.current} * {
          -webkit-user-select: none !important;
          user-select: none !important;
          -webkit-touch-callout: none !important;
        }
      `;
      document.head.appendChild(style);
    }

    const playerId = playerIdRef.current;
    const script = document.createElement("script");
    script.type = "module";
    script.dataset.gcorePlayerExample = playerId;
    script.textContent = `
      import {
        BigMuteButton,
        BottomGear,
        ErrorScreen,
        MediaControl,
        Player,
        QualityLevels,
        SourceController,
        Spinner,
      } from "${playerModuleUrl}";

      const container = document.getElementById(${JSON.stringify(playerId)});

      if (container) {
        window.__gcoreMintlifyPlayers = window.__gcoreMintlifyPlayers || {};

        if (!window.__gcoreMintlifyPlayerPluginsRegistered) {
          Player.registerPlugin(MediaControl);
          Player.registerPlugin(SourceController);
          Player.registerPlugin(Spinner);
          Player.registerPlugin(ErrorScreen);
          Player.registerPlugin(BigMuteButton);
          Player.registerPlugin(BottomGear);
          Player.registerPlugin(QualityLevels);
          window.__gcoreMintlifyPlayerPluginsRegistered = true;
        }

        const existingPlayer = window.__gcoreMintlifyPlayers[${JSON.stringify(playerId)}];
        if (existingPlayer?.destroy) {
          existingPlayer.destroy();
        }

        const player = new Player({
          autoPlay: true,
          mute: true,
          sources: [${JSON.stringify(resolvedSource)}],
          spinner: {
            showOnError: true,
            showOnStart: true,
          },
        });

        player.attachTo(container);
        window.__gcoreMintlifyPlayers[${JSON.stringify(playerId)}] = player;
      }
    `;

    document.body.appendChild(script);

    return () => {
      const player = window.__gcoreMintlifyPlayers?.[playerId];
      if (player?.destroy) {
        player.destroy();
      }

      if (window.__gcoreMintlifyPlayers) {
        delete window.__gcoreMintlifyPlayers[playerId];
      }

      script.remove();

      if (containerRef.current) {
        containerRef.current.innerHTML = "";
      }
    };
  }, [resolvedSource]);

  return (
    <div className="not-prose my-6">
      <div
        className="overflow-hidden rounded-2xl border border-zinc-950/10 dark:border-white/10"
        style={{
          background:
            "linear-gradient(180deg, rgba(17, 24, 39, 0.04), rgba(17, 24, 39, 0.08))",
        }}
      >
        <div
          id={playerIdRef.current}
          ref={containerRef}
          className="w-full"
          style={{ aspectRatio: "16 / 9", minHeight: "320px" }}
        />
      </div>
    </div>
  );
};

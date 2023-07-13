---
title: prometheus-exporter
displayName: 'Prometheus xporter'
published: true
order: 40
toc:
   --1--What is Prometheus exporter?: what-is-prometheus-exporter
   --1--How does it work?: how-does-it-work
   --1--Key metrics: key-metrics
---
# Prometheus exporter

## What is Prometheus exporter?

The Prometheus exporter is a service that offers OpenSearch index metrics to clients. It provides secure access to user-specific metrics for authenticated users. 

## How does it work?

You configure your Prometheus target, providing the Prometheus exporter endpoint and your Logging credentials using HTTPS Basic Authentication. For example, the Prometheus target configuration for Luxembourg would look like this:

<code-block>
 - job_name: 'your_awesome_job'
    scrape_interval: 5m
    scrape_timeout: 30s
    scheme: https
    static_configs:
        - targets: ['<span style="color:#FF5913">laas-exporter.k1.luxembourg-1.cloud.gcore.com</span>']
    metrics_path: "/v1/opensearch/indices/metrics"
    basic_auth:
      username: '<span style="color:#FF5913">yourLoggingUsername</span>'
      password: '<span style="color:#FF5913">yourLoggingPassword</span>'
</code-block>

The Prometheus exporter endpoint for your region in specified in your control panel. 

## Understand the key metrics

The table below explains the key metrics provided by the Prometheus exporter. These metrics offer valuable insights into the health and usage of your Logging environment.

<table>
   <tr>
      <td>Metric</td>
      <td>Description</td>
      <td>Type</td>
   </tr>
   <tr>
      <td>opensearch_index_stats_index_current</td>
      <td>The number of documents currently being indexed to a specific index</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_index_stats_query_cache_size</td>
      <td>The total size of the query cache</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_index_stats_search_scroll_current</td>
      <td>The current count of search scrolls</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_completion_bytes_primary</td>
      <td>The current size of completion data with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_deleted_docs_primary</td>
      <td>The count of deleted documents with only primary shards</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_docs_primary</td>
      <td>The count of documents with only primary shards</td>
      <td>gauge</td>
   </tr>      
   <tr>
      <td>opensearch_indices_mappings_stats_fields</td>
      <td>The current number of fields within the cluster</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_count_primary </td>
      <td>The current number of segments with only primary shards across all nodes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_doc
      _values_memory_bytes_primary</td>
      <td>The current size of doc values with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_segment_fields
      _memory_bytes_primary</td>
      <td>The current size of fields with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_indices_segment_fixed
      _bit_set_memory_bytes_primary</td>
      <td>The current size of fixed bit sets with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_index
      _writer_memory_bytes_primary</td>
      <td>The current size of index writer with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>      
   <tr>
      <td>opensearch_indices_segment
      _memory_bytes_primary</td>
      <td>The current size of segments with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_segment
      _norms_memory_bytes_primary</td>
      <td>The current size of norms with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_segment
      _points_memory_bytes_primary</td>
      <td>The current size of points with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_segment
      _term_vectors_memory_primary_bytes</td>
      <td>The current size of term vectors with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_indices_segment
      _terms_memory_primary</td>
      <td>The current size of terms with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment
      _version_map_memory_bytes_primary</td>
      <td>The current size of version map with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>    
   <tr>
      <td>opensearch_indices_settings
      _total_fields</td>
      <td>The index mapping setting for “total_fields”</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_store_size
      _bytes_primary</td>
      <td>The current total size of stored index data in bytes with only primary shards across all nodes</td>
      <td>gauge</td>
   </tr>     
   <tr>
      <td>opensearch_search_active_queries</td>
      <td>The number of currently active queries</td>
      <td>gauge</td>
   </tr>
</table>


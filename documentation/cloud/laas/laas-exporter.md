---
title: laas-exporter
displayName: LaaS Exporter
published: false
order: 40
toc:
   --1--What is LaaS Exporter?: "what-is-laas-exporter"
   --1--How does it work?: "how-does-laas-exporter-work"
   --1--Key metrics: "understand-the-key-metrics"
---
# LaaS Exporter

## What is LaaS Exporter?

The LaaS Exporter is a service that offers LaaS OpenSearch index metrics to clients. It provides secure access to user-specific metrics for authenticated users. 

## How does LaaS Exporter work?

You configure your Prometheus target, providing the LaaS Exporter endpoint and your LaaS credentials using HTTPS Basic Authentication. For example, the Prometheus target configuration for Luxembourg would look like this:

```
 - job_name: 'your_awesome_job'
    scrape_interval: 5m
    scrape_timeout: 30s
    scheme: https
    static_configs:
        - targets: ['laas-exporter.k1.luxembourg-1.cloud.gcore.com']
    metrics_path: "/v1/opensearch/indices/metrics"
    basic_auth:
      username: 'yourLaasUsername'
      password: 'yourLaasPassword'
```

The LaaS endpoint for your region in specified in your control panel. 

## Understand the key metrics

The table below explains the key metrics provided by the LaaS Exporter. These metrics offer valuable insights into the health and usage of your LaaS environment.

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
      <td>opensearch_indices_completion_bytes_total</td>
      <td>The current size of completion data with all shards across all nodes </td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_deleted_docs_primary</td>
      <td>The count of deleted documents with only primary shards</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_deleted_docs_total </td>
      <td>The total count of deleted documents</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_docs_primary</td>
      <td>The count of documents with only primary shards</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_docs_total </td>
      <td>The total count of documents</td>
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
      <td>opensearch_indices_segment_count_total</td>
      <td>The current number of segments with all shards across all nodes</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_indices_segment_doc_values_memory_bytes_primary</td>
      <td>The current size of doc values with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_doc_values_memory_bytes_total</td>
      <td>The current size of doc values with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_fields_memory_bytes_primary</td>
      <td>The current size of fields with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_indices_segment_fields_memory_bytes_total</td>
      <td>The current size of fields with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>
   <tr>
      <td>opensearch_indices_segment_fixed_bit_set_memory_bytes_primary</td>
      <td>The current size of fixed bit sets with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_fixed_bit_set_memory_bytes_total </td>
      <td>The current size of fixed bit sets with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_index_writer_memory_bytes_primary</td>
      <td>The current size of index writer with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_index_writer_memory_bytes_total</td>
      <td>The current size of index writer with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_memory_bytes_primary</td>
      <td>The current size of segments with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>    
   <tr>
      <td>opensearch_indices_segment_memory_bytes_total</td>
      <td>The current size of segments with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_norms_memory_bytes_primary</td>
      <td>The current size of norms with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_norms_memory_bytes_total </td>
      <td>The current size of norms with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_points_memory_bytes_primary</td>
      <td>The current size of points with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_points_memory_bytes_total</td>
      <td>The current size of points with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_term_vectors_memory_primary_bytes</td>
      <td>The current size of term vectors with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_term_vectors_memory_total_bytes</td>
      <td>The current size of term vectors with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_terms_memory_primary</td>
      <td>The current size of terms with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_terms_memory_total </td>
      <td>The current size of terms with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_version_map_memory_bytes_primary</td>
      <td>The current size of version map with only primary shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_segment_version_map_memory_bytes_total</td>
      <td>The current size of the version map with all shards across all nodes in bytes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_settings_total_fields</td>
      <td>The index mapping setting for “total_fields”</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_store_size_bytes_primary</td>
      <td>The current total size of stored index data in bytes with only primary shards across all nodes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_indices_store_size_bytes_total</td>
      <td>The current total size of stored index data in bytes with all shards across all nodes</td>
      <td>gauge</td>
   </tr>   
   <tr>
      <td>opensearch_search_active_queries</td>
      <td>The number of currently active queries</td>
      <td>gauge</td>
   </tr>
</table>


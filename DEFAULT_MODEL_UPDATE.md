# Default Model Update - Change Summary

## Change Made
Updated the default embedding model from `nomic-embed-text` to `all-MiniLM-L6-v2` in the Ollama embedding configuration.

## Files Modified

### 1. `src/chroma_mcp/server.py`
- **Function**: `_ollama_embedding_factory()`
- **Change**: Updated default value for `EMBEDDINGS_MODEL` environment variable
- **Before**: `os.getenv("EMBEDDINGS_MODEL", "nomic-embed-text")`
- **After**: `os.getenv("EMBEDDINGS_MODEL", "all-MiniLM-L6-v2")`

### 2. `README.md`
- **Section**: Embedding Function Environment Variables
- **Change**: Updated example default value in documentation
- **Before**: `export EMBEDDINGS_MODEL="nomic-embed-text"`
- **After**: `export EMBEDDINGS_MODEL="all-MiniLM-L6-v2"`

### 3. `.chroma_env.example`
- **Change**: Updated example environment configuration
- **Before**: `EMBEDDINGS_MODEL=nomic-embed-text`
- **After**: `EMBEDDINGS_MODEL=chroma/all-MiniLM-L6-v2-f32
- **Note**: Added `nomic-embed-text` as alternative option in comments

### 4. `OLLAMA_IMPLEMENTATION.md`
- **Section**: Environment Variable Support & Configuration Examples
- **Change**: Updated default model references throughout the document
- **Before**: Default model listed as `nomic-embed-text`
- **After**: Default model listed as `chroma/all-MiniLM-L6-v2-f32`

## Verification Results

✅ **Factory Function Test**: Successfully creates `OllamaEmbeddingFunction` with `all-MiniLM-L6-v2` model
✅ **Environment Override Test**: Confirmed environment variables still work for overriding the default
✅ **Collection Creation Test**: Collections are created successfully using the new default model
✅ **Documentation Consistency**: All documentation updated to reflect the new default

## Impact

- **Backwards Compatibility**: ✅ Maintained - users can still use `nomic-embed-text` by setting the environment variable
- **Default Behavior**: ✅ Changed - new installations will use `all-MiniLM-L6-v2` by default
- **Existing Collections**: ✅ Unaffected - existing collections retain their original embedding function configuration

## Notes

- `all-MiniLM-L6-v2` is a popular and efficient sentence transformer model
- The model provides good performance for most embedding tasks
- Users can still override this default by setting the `EMBEDDINGS_MODEL` environment variable
- The change is immediately effective for new collection creations

import vcr

myvcr = vcr.VCR(
    cassette_library_dir="fixtures/cassettes",
    record_mode="once",
    match_on=["uri", "method"],
    )

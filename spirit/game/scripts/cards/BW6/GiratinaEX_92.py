from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.bw10 import big_swing, shred

card = PokemonCardDef(
    guid="4a58e7b0-f2be-5640-85f1-e02f5bae9a7a",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaEX.Name",
    display_name="Giratina-EX",
    searchable_by=["Giratina-EX","Basic","EX","GiratinaEX"],
    subtypes=["Basic","EX"],
    collector_number=92,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=shred,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=mill_attack(3, opponent=False),
        ),
    ],
)

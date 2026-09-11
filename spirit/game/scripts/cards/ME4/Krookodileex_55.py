from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="93fc82b8-ad2f-5197-973a-dc4f77eba956",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodileex.Name",
    display_name="Krookodile ex",
    searchable_by=["Krookodile ex", "Stage 2", "ex", "Krookodileex"],
    subtypes=["Stage 2", "ex"],
    collector_number=55,
    set_code="ME4",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=553,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title="Strong Bite",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)

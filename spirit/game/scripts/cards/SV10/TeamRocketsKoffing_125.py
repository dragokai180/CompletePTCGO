from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a8cb95d1-ab44-57c6-93a3-a966fc230e8d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKoffing.Name",
    display_name="Team Rocket's Koffing",
    searchable_by=["Team Rocket's Koffing", "Basic", "TeamRocketsKoffing"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=109,
    abilities=[
        Ability(
            title="Smog Signals",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), search your deck for up to 2 Pokémon that have \"Koffing\" in their name and put them onto your Bench. Then, shuffle your deck.",
            passive=standard_passive("If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), search your deck for up to 2 Pokémon that have \"Koffing\" in their name and put them onto your Bench. Then, shuffle your deck."),
        ),
        Attack(
            title="Leaking Gas",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3a447af6-a1b6-51c5-bc9b-7d0dad0b9add",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArbok.Name",
    display_name="Team Rocket's Arbok",
    searchable_by=["Team Rocket's Arbok", "Stage 1", "TeamRocketsArbok"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsEkans.Name",
    family_id=23,
    abilities=[
        Ability(
            title="Potent Glare",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Pokémon that has an Ability from their hand, except for Team Rocket's Pokémon.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, your opponent can't play any Pokémon that has an Ability from their hand, except for Team Rocket's Pokémon."),
        ),
        Attack(
            title="Spinning Tail",
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 3},
            effect=standard_attack,
        ),
    ],
)

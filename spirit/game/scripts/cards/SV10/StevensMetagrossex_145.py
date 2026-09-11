from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4a0d8bd5-1e64-5467-813f-d99e1e4eeffe",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetagrossex.Name",
    display_name="Steven's Metagross ex",
    searchable_by=["Steven's Metagross ex", "Stage 2", "ex", "StevensMetagrossex"],
    subtypes=["Stage 2", "ex"],
    collector_number=145,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="X-Boot",
            game_text="Once during your turn, you may search your deck for a Basic Psychic Energy card, a Basic Metal Energy card, or 1 of each and attach them to your Psychic Pokémon and Metal Pokémon in any way you like. Then, shuffle your deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Metal Stomp",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
        ),
    ],
)

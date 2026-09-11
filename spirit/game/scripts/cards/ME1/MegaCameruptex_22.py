from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="fbea03e7-630c-5178-a296-821dba756813",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCameruptex.Name",
    display_name="Mega Camerupt ex",
    searchable_by=["Mega Camerupt ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaCameruptex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=22,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If your opponent's Active Pokémon is Burned, this attack does 160 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Volcanic Meteor",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=280,
            effect=standard_attack,
        ),
    ],
)

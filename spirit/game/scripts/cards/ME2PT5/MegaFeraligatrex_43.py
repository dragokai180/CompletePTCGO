from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="81613fe3-f926-5c6a-b464-eae79714dbf7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFeraligatrex.Name",
    display_name="Mega Feraligatr ex",
    searchable_by=["Mega Feraligatr ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaFeraligatrex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=43,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=370,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Mortal Crunch",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)

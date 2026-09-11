from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4bb0b950-e32f-548a-868e-32b725f3d9c0",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGengarex.Name",
    display_name="Mega Gengar ex",
    searchable_by=["Mega Gengar ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaGengarex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=56,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadowy Concealment",
            game_text="If 1 of your Darkness Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack.",
            passive=standard_passive("If 1 of your Darkness Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack."),
        ),
        Attack(
            title="Void Gale",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=standard_attack,
        ),
    ],
)

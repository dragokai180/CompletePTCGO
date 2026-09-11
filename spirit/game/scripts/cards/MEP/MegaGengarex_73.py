from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="916efd31-c92b-506f-ab20-372c60557ed4",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGengarex.Name",
    display_name="Mega Gengar ex",
    searchable_by=["Mega Gengar ex", "Stage 2", "MegaGengarex"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    abilities=[
        Ability(
            title="Shadowy Concealment",
            game_text="If 1 of your [ [Darkness] ] Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack.",
            passive=standard_passive("If 1 of your [ [Darkness] ] Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack."),
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

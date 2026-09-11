from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3e6e22f0-ceb7-5c70-88bf-0164a3f96882",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleonex.Name",
    display_name="Empoleon ex",
    searchable_by=["Empoleon ex", "Stage 2", "ex", "Empoleonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=70,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Emperor's Stance",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=standard_passive("Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)"),
        ),
        Attack(
            title="Iron Feathers",
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df2c2524-c7c8-5335-a9fa-a922c596f5f0',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name',
    display_name='Blastoise',
    searchable_by=['Blastoise', 'Stage 2', 'Blastoise'],
    subtypes=['Stage 2'],
    collector_number=13,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    family_id=7,
    abilities=[
        Ability(
            title='Wash Out',
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy attached to 1 of your Benched Pokémon to your Active Pokémon. This power can't be used if Blastoise is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Hydro Launcher',
            game_text="Return 2 Water Energy attached to Blastoise to your hand. Choose 1 of your opponent's Pokémon. This attack does 100 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)

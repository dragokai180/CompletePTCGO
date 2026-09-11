from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b17e3eb-a1b6-502a-bf2a-50ae9d25c427',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name',
    display_name='Ludicolo',
    searchable_by=['Ludicolo', 'Stage 2', 'Ludicolo'],
    subtypes=['Stage 2'],
    collector_number=2,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name',
    family_id=272,
    abilities=[
        Ability(
            title='Table Service',
            game_text='Once during your turn (before your attack), you may heal 30 damage from 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Punch and Run',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

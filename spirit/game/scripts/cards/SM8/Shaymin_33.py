from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b821ac9e-c450-57fa-a6ee-eac5f2992f71',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    display_name='Shaymin',
    searchable_by=['Shaymin', 'Basic', 'Shaymin'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=492,
    abilities=[
        Ability(
            title='Floral Heal',
            game_text='Once during your turn (before your attack), you may heal 20 damage from your Active Grass Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='971f22bc-2a67-59c4-a08e-cf54638b5e93',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    display_name='Bidoof',
    searchable_by=['Bidoof', 'Basic', 'Bidoof'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=399,
    abilities=[
        Attack(
            title='Drench',
            game_text='If this Pokémon has any Water Energy attached to it, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When this Pokémon is healed, double the amount healed.'),
)

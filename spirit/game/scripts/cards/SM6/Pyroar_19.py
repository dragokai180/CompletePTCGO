from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6bfdb52f-dfa8-55ac-b30f-066f05fea919',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Ability(
            title='Unnerve',
            game_text='Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.',
            passive=standard_passive('Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.'),
        ),
        Attack(
            title='Dominating Fangs',
            game_text='If Lysandre Labs is in play, this attack does 60 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

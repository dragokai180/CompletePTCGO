from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78f37d2c-8ebb-50df-91cd-158db6b5c399',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name',
    display_name='Feraligatr',
    searchable_by=['Feraligatr', 'Stage 2', 'Feraligatr'],
    subtypes=['Stage 2'],
    collector_number=24,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    family_id=158,
    abilities=[
        Ability(
            title='Downpour',
            game_text='As often as you like during your turn (before your attack), you may discard a Water Energy card from your hand.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Riptide',
            game_text='This attack does 20 more damage for each Water Energy card in your discard pile. Then, shuffle those cards into your deck.',
            cost={PokemonTypes.WATER: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

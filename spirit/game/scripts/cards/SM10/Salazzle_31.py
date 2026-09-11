from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a543306-198c-5c30-8f52-a16b1773083f',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name',
    display_name='Salazzle',
    searchable_by=['Salazzle', 'Stage 1', 'Salazzle'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    family_id=757,
    abilities=[
        Ability(
            title='Roast Reveal',
            game_text='Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3b3138d-324c-5157-a369-dcbd0ef91c7b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name',
    display_name='Silvally-GX',
    searchable_by=['Silvally-GX', 'Stage 1', 'GX', 'SilvallyGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=91,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    family_id=773,
    abilities=[
        Ability(
            title='Gyro Unit',
            game_text='Your Basic Pokémon in play have no Retreat Cost.',
            passive=standard_passive('Your Basic Pokémon in play have no Retreat Cost.'),
        ),
        Attack(
            title='Turbo Drive',
            game_text='Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Rebel-GX',
            game_text="This attack does 50 damage for each of your opponent's Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)

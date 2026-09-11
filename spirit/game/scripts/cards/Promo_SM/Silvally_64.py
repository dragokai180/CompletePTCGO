from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='abea2da9-069b-57ee-9f51-87dee3f78ad2',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Silvally.Name',
    display_name='Silvally',
    searchable_by=['Silvally', 'Stage 1', 'Silvally'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    family_id=773,
    abilities=[
        Attack(
            title='Gear Scan',
            game_text='Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

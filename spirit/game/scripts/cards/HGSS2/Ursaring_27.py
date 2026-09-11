from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dfce3c61-6ecf-5bd7-94f4-98089acde512',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name',
    display_name='Ursaring',
    searchable_by=['Ursaring', 'Stage 1', 'Ursaring'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    family_id=216,
    abilities=[
        Attack(
            title='Confront',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Cross Chop',
            game_text='Flip a coin. If heads, this attack does 50 damage plus 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

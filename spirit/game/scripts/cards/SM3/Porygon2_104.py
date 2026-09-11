from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4788aacb-cded-5093-abde-4437d1935481',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    display_name='Porygon2',
    searchable_by=['Porygon2', 'Stage 1', 'Porygon2'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    family_id=137,
    abilities=[
        Attack(
            title='Calculate',
            game_text='Look at the top 6 cards of your deck and put them back in any order.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Beam',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

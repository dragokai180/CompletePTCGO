from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20a5d928-06f4-5190-b7f7-864d9c2711a4',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name',
    display_name='Hariyama',
    searchable_by=['Hariyama', 'Stage 1', 'Hariyama'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    family_id=296,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Backward Belt Throw',
            game_text='You may do 80 damage plus 20 more damage. If you do, Hariyama does 20 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

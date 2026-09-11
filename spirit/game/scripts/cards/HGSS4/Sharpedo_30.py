from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f37fc693-2461-5900-8c63-8d733675eb8d',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name',
    display_name='Sharpedo',
    searchable_by=['Sharpedo', 'Stage 1', 'Sharpedo'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    family_id=318,
    abilities=[
        Attack(
            title='Strip Bare',
            game_text='Flip 2 coins. If both of them are heads, your opponent discards all card from his or her hand.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Rage',
            game_text='Does 50 damage plus 10 more damage for each damage counter on Sharpedo.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

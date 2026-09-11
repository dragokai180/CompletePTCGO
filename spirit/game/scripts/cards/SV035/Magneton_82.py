from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08da1251-3bc6-5e43-988b-ed8df27f71d2',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    display_name='Magneton',
    searchable_by=['Magneton', 'Stage 1', 'Magneton'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    family_id=81,
    abilities=[
        Attack(
            title='Junk Magnet',
            game_text='Put up to 2 Item cards from your discard pile into your hand.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)

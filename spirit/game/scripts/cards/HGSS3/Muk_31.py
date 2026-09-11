from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10a01069-b6e1-5953-9fb0-9c79adbf2e39',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name',
    display_name='Muk',
    searchable_by=['Muk', 'Stage 1', 'Muk'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    family_id=88,
    abilities=[
        Attack(
            title='Sludge Drag',
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon. The new Defending Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pester',
            game_text='If the Defending Pokémon is affected by a Special Condition, this attack does 50 damage plus 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

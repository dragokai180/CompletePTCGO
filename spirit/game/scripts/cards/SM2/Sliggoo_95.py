from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='43f84e89-6638-5b82-a7d2-68f883faa2ab',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    display_name='Sliggoo',
    searchable_by=['Sliggoo', 'Stage 1', 'Sliggoo'],
    subtypes=['Stage 1'],
    collector_number=95,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name',
    family_id=704,
    abilities=[
        Attack(
            title='Division',
            game_text='Search your deck for up to 2 Sliggoo and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89ea189d-4b1d-506d-be53-33c9e645c0f5',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name',
    display_name='Weavile',
    searchable_by=['Weavile', 'Stage 1', 'Weavile'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    family_id=215,
    abilities=[
        Attack(
            title='Nasty Plot',
            game_text='Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)

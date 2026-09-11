from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a91ac1e-b6c5-5a19-a8d5-14cbf2ca9451',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name',
    display_name='Parasect',
    searchable_by=['Parasect', 'Stage 1', 'Parasect'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    family_id=46,
    abilities=[
        Attack(
            title='Colorful Spores',
            game_text='Choose 3 of your Pokémon. For each of those Pokémon, search your deck for a different type of basic Energy card and attach it to that Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

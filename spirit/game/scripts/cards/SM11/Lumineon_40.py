from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd5436af-5196-5a37-8f0e-ed77ba0ff232',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name',
    display_name='Lumineon',
    searchable_by=['Lumineon', 'Stage 1', 'Lumineon'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name',
    family_id=456,
    abilities=[
        Attack(
            title='Neon Trickery',
            game_text="You may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

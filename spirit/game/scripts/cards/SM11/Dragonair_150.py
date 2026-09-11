from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d735b87-3bbc-5570-9d15-e926b82e7923',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    display_name='Dragonair',
    searchable_by=['Dragonair', 'Stage 1', 'Dragonair'],
    subtypes=['Stage 1'],
    collector_number=150,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Destructive Whirlpool',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

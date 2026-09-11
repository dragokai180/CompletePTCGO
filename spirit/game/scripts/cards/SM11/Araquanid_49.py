from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e04a6d25-0e82-578a-a14a-fcf644993d6a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name',
    display_name='Araquanid',
    searchable_by=['Araquanid', 'Stage 1', 'Araquanid'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    family_id=751,
    abilities=[
        Attack(
            title='Tangle Drag',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sticky Web',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

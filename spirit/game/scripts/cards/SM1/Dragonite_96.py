from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b33a1582-e923-532f-bb0a-37d4e3150744',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name',
    display_name='Dragonite',
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=96,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Dragon Wave',
            game_text='Discard a Grass Energy and a Lightning Energy from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            effect=standard_attack,
        ),
        Attack(
            title='Giant Tail',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 5},
            damage=200,
            effect=standard_attack,
        ),
    ],
)

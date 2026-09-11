from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a95150fc-a3e2-5222-a1a8-a75eca1aeca5',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name',
    display_name='Probopass',
    searchable_by=['Probopass', 'Stage 1', 'Probopass'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    family_id=299,
    abilities=[
        Attack(
            title='Bounce Back',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Rock Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

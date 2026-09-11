from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cdb9593b-2789-5a6e-bbcc-924eebfbc7ad',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name',
    display_name='Stoutland',
    searchable_by=['Stoutland', 'Stage 2', 'Stoutland'],
    subtypes=['Stage 2'],
    collector_number=105,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    family_id=506,
    abilities=[
        Attack(
            title='Ferocious Bellow',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)

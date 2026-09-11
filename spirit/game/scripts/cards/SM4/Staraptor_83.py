from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c36f83f-248b-5062-8352-8aa713a8353a',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name',
    display_name='Staraptor',
    searchable_by=['Staraptor', 'Stage 2', 'Staraptor'],
    subtypes=['Stage 2'],
    collector_number=83,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name',
    family_id=396,
    abilities=[
        Attack(
            title='Clutch',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Sky Hunting',
            game_text="If your opponent's Pokémon is Knocked Out by the damage from this attack, switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

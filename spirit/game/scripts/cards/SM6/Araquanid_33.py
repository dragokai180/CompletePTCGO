from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='59ee9eb6-6bfc-5a27-8d0b-afee84e97ca6',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name',
    display_name='Araquanid',
    searchable_by=['Araquanid', 'Stage 1', 'Araquanid'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
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
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Bubble Trap',
            game_text='If 1 of your Pokémon used Bubble during your last turn, this attack does 80 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

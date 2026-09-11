from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a13d091-f253-5a0f-9548-7780064095c2',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name',
    display_name='Zygarde',
    searchable_by=['Zygarde', 'Basic', 'Zygarde'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Attack(
            title='Rumble',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Raging Blade',
            game_text='If this Pokémon has any damage counters on it, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

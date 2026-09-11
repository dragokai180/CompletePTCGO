from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c6ec059-6582-5c21-802a-831fd44ce2f0',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    display_name='Scyther',
    searchable_by=['Scyther', 'Basic', 'Scyther'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=123,
    abilities=[
        Attack(
            title='Twin Play',
            game_text='Search your deck for up to 2 Scyther and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Agility',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

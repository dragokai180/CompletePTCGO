from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8c0e0eb-bab8-5d40-8644-2a2589e7cc35',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name',
    display_name='Arceus ◇',
    searchable_by=['Arceus ◇', 'Basic', 'Prism Star', 'Arceus'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=96,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=493,
    abilities=[
        Ability(
            title='First Law',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon.",
            passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to this Pokémon."),
        ),
        Attack(
            title='Trinity Star',
            game_text='You can use this attack only if you have Grass, Water, and Lightning Pokémon on your Bench. Search your deck for up to 3 basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

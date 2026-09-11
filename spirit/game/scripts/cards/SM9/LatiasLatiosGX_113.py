from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed5bbef1-8c52-51ca-a97e-ae8b8cb52964',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LatiasLatiosGX.Name',
    display_name='Latias & Latios-GX',
    searchable_by=['Latias & Latios-GX', 'Basic', 'TAG TEAM', 'GX', 'LatiasLatiosGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=113,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=380,
    abilities=[
        Attack(
            title='Buster Purge',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=standard_attack,
        ),
        Attack(
            title='Aero Unit-GX',
            game_text="Attach 5 basic Energy cards from your discard pile to your Pokémon in any way you like. If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), prevent all effects of attacks, including damage, done to it during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)

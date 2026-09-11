from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fa6deb1-58f7-5705-a69c-531db08832d5',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaZoroarkGX.Name',
    display_name='Greninja & Zoroark-GX',
    searchable_by=['Greninja & Zoroark-GX', 'Basic', 'TAG TEAM', 'GX', 'GreninjaZoroarkGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=107,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=571,
    abilities=[
        Attack(
            title='Dark Pulse',
            game_text='This attack does 30 more damage times the amount of Darkness Energy attached to all of your Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dark Union-GX',
            game_text="Put 2 in any combination of Darkness Pokémon-GX and Darkness Pokémon-EX from your discard pile onto your Bench. If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), attach 2 Energy cards from your discard pile to each Pokémon that you put onto your Bench in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

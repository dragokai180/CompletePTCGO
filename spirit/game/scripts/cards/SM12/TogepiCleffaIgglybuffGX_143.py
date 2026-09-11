from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6e369a2-16d2-52f5-87ec-6c754c526889',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TogepiCleffaIgglybuffGX.Name',
    display_name='Togepi & Cleffa & Igglybuff-GX',
    searchable_by=['Togepi & Cleffa & Igglybuff-GX', 'Basic', 'TAG TEAM', 'GX', 'TogepiCleffaIgglybuffGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=143,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=173,
    abilities=[
        Attack(
            title='Rolling Panic',
            game_text='Flip a coin until you get tails. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Supreme Puff-GX',
            game_text="Take another turn after this one. (Skip the between-turns step.) If this Pokémon has at least 14 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles all of their Benched Pokémon and all cards attached to them into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

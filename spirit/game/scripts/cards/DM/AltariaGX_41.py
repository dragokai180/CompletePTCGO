from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='471f8ec7-f921-5027-bacf-271e83686ce1',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AltariaGX.Name',
    display_name='Altaria-GX',
    searchable_by=['Altaria-GX', 'Stage 1', 'GX', 'AltariaGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=41,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Attack(
            title='Bright Tone',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Pokémon-GX and Pokémon-EX.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Sonic Edge',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
        Attack(
            title='Euphoria-GX',
            game_text="Your opponent's Active Pokémon is now Asleep. Heal all damage from all of your Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

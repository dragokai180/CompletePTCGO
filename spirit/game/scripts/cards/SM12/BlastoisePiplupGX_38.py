from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1ae6513a-d2e0-51b9-8613-a7698f5e1276',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoisePiplupGX.Name',
    display_name='Blastoise & Piplup-GX',
    searchable_by=['Blastoise & Piplup-GX', 'Basic', 'TAG TEAM', 'GX', 'BlastoisePiplupGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=38,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=9,
    abilities=[
        Attack(
            title='Splash Maker',
            game_text='You may attach up to 3 Water Energy cards from your hand to your Pokémon in any way you like. If you do, heal 50 damage from those Pokémon for each card you attached to them in this way.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Bubble Launcher-GX',
            game_text="Your opponent's Active Pokémon is now Paralyzed. If this Pokémon has at least 3 extra Water Energy attached to it (in addition to this attack's cost), this attack does 150 more damage. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
            gx=True,
        ),
    ],
)

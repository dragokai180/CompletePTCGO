from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69a11422-42ab-5690-9883-fad91063546a',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaGX.Name',
    display_name='Rayquaza-GX',
    searchable_by=['Rayquaza-GX', 'Basic', 'GX', 'RayquazaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=109,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Ability(
            title='Stormy Winds',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may discard the top 3 cards of your deck. If you do, attach a basic Energy card from your discard pile to this Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Dragon Break',
            game_text='This attack does 30 damage times the amount of basic Grass and basic Lightning Energy attached to your Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Tempest-GX',
            game_text="Discard your hand and draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

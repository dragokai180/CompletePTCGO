from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='26dad21b-ef22-54a5-bac9-e4dab20686d0',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PrimalGroudonEX.Name',
    display_name='Primal Groudon-EX',
    searchable_by=['Primal Groudon-EX', 'MEGA', 'EX', 'PrimalGroudonEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=86,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name',
    family_id=383,
    abilities=[
        Attack(
            title='Gaia Volcano',
            game_text='If there is any Stadium card in play, this attack does 100 more damage. Discard that Stadium card.',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.'),
)

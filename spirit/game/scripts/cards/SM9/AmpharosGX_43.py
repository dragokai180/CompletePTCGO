from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a10b79b-a809-506d-b91d-f740693ec621',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosGX.Name',
    display_name='Ampharos-GX',
    searchable_by=['Ampharos-GX', 'Stage 2', 'GX', 'AmpharosGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=43,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    family_id=179,
    abilities=[
        Attack(
            title='Power Recharge',
            game_text='Put all Electropower cards from your discard pile into your hand.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Impact Bolt',
            game_text='Discard all Lightning Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Electrical-GX',
            game_text="Search your deck for up to 7 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)

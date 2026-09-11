from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='10d3760e-c1cd-52b4-bcfc-45fdc9a916ae',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garchompex.Name',
    display_name='Garchomp ex',
    searchable_by=['Garchomp ex', 'Stage 2', 'Tera', 'ex', 'Garchompex'],
    subtypes=['Stage 2', 'Tera', 'ex'],
    collector_number=38,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Hydro Lander',
            game_text='Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pokémon in any way you like.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Sonic Dive',
            game_text="Discard 2 Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

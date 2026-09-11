from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="fae1b06f-89aa-5c40-92b2-f006aa122d89",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidoriex.Name",
    display_name="Munkidori ex",
    searchable_by=["Munkidori ex", "Basic", "ex", "Munkidoriex"],
    subtypes=["Basic", "ex"],
    collector_number=37,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1015,
    abilities=[
        Ability(
            title="Oh No You Don't",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card.",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card."),
        ),
        Attack(
            title="Dirty Headbutt",
            game_text="During your next turn, this Pokémon can't use Dirty Headbutt.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
